const API = 'https://finance-tracker-api-4m7d.onrender.com'

// ─── SUMMARY ───────────────────────────────────────
function loadSummary() {
    fetch(`${API}/transactions/summary`)
        .then(r => r.json())
        .then(data => {
            document.getElementById('balance').textContent = `$${data.balance}`
            document.getElementById('total-income').textContent = `$${data.total_income}`
            document.getElementById('total-expenses').textContent = `$${data.total_expenses}`
        })
}

// ─── TRANSACTIONS ───────────────────────────────────
function loadTransactions() {
    fetch(`${API}/transactions`)
        .then(r => r.json())
        .then(data => {
            const list = document.getElementById('transactions-list')
            list.innerHTML = ''
            data.forEach(t => {
                list.innerHTML += `
                <div class="transaction-item ${t.type}">
                    <div>
                        <strong>${t.description}</strong>
                        <p style="font-size:12px; opacity:0.7">${t.category} • ${t.date}</p>
                    </div>
                    <div style="display:flex; align-items:center; gap:10px">
                        <span class="transaction-amount ${t.type}">
                            ${t.type === 'income' ? '+' : '-'}$${t.amount}
                        </span>
                        <button class="delete-btn" onclick="deleteTransaction(${t.id})">✕</button>
                    </div>
                </div>`
            })
        })
}

function addTransaction() {
    const amount = document.getElementById('amount').value
    const category = document.getElementById('category').value
    const type = document.getElementById('type').value
    const date = document.getElementById('date').value
    const description = document.getElementById('description').value

    fetch(`${API}/transactions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ amount, category, type, date, description })
    })
    .then(r => r.json())
    .then(() => {
        loadTransactions()
        loadSummary()
    })
}

function deleteTransaction(id) {
    fetch(`${API}/transactions/${id}`, { method: 'DELETE' })
        .then(r => r.json())
        .then(() => {
            loadTransactions()
            loadSummary()
        })
}

// ─── PORTFOLIO ──────────────────────────────────────
function loadPortfolio() {
    fetch(`${API}/portfolio`)
        .then(r => r.json())
        .then(data => {
            const list = document.getElementById('portfolio-list')
            list.innerHTML = ''
            data.forEach(stock => {
                const isProfit = stock.profit_loss >= 0
                list.innerHTML += `
                <div class="portfolio-item">
                    <div style="display:flex; justify-content:space-between">
                        <strong>${stock.stock_name} (${stock.symbol})</strong>
                        <button class="delete-btn" onclick="deleteStock(${stock.id})">✕</button>
                    </div>
                    <p style="font-size:12px; opacity:0.7">
                        ${stock.shares} shares • Bought @ $${stock.purchase_price}
                    </p>
                    <div style="display:flex; justify-content:space-between; margin-top:8px">
                        <span>Current: $${stock.current_price ?? 'N/A'}</span>
                        <span class="${isProfit ? 'profit' : 'loss'}">
                            ${isProfit ? '+' : ''}$${stock.profit_loss ?? 'N/A'}
                        </span>
                    </div>
                </div>`
            })
        })
}

function addStock() {
    const stock_name = document.getElementById('stock-name').value
    const symbol = document.getElementById('symbol').value
    const shares = document.getElementById('shares').value
    const purchase_price = document.getElementById('purchase-price').value
    const purchase_date = document.getElementById('purchase-date').value

    fetch(`${API}/portfolio`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stock_name, symbol, shares, purchase_price, purchase_date })
    })
    .then(r => r.json())
    .then(() => loadPortfolio())
}

function deleteStock(id) {
    fetch(`${API}/portfolio/${id}`, { method: 'DELETE' })
        .then(r => r.json())
        .then(() => loadPortfolio())
}

// ─── NEWS ───────────────────────────────────────────
function loadNews() {
    fetch(`${API}/news`)
        .then(r => r.json())
        .then(displayNews)
}

function loadStockNews() {
    const symbol = document.getElementById('news-symbol').value
    if (!symbol) return loadNews()
    fetch(`${API}/news/stock?symbol=${symbol}`)
        .then(r => r.json())
        .then(displayNews)
}

function displayNews(articles) {
    const list = document.getElementById('news-list')
    list.innerHTML = ''
    articles.forEach(article => {
        list.innerHTML += `
        <div class="news-item">
            <h3>${article.title}</h3>
            <p>${article.description ?? 'No description available'}</p>
            <a href="${article.url}" target="_blank">Read more →</a>
        </div>`
    })
}

// ─── INIT ───────────────────────────────────────────
loadSummary()
loadTransactions()
loadPortfolio()
loadNews()