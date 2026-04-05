function loadSummary(){
    fetch('http://127.0.0.1:5000/transactions/summary')
    .then(response => response.json())
    .then(data => {
        document.getElementById('balance').textContent = data.balance
        document.getElementById('total-income').textContent = data.total_income
        document.getElementById('total-expenses').textContent = data.total_expenses
    })
}

function loadTransactions(){
    fetch('http://127.0.0.1:5000/transactions')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('transactions')
        container.innerHTML = ''
        data.forEach(transaction => {
            container.innerHTML += ` 
                <div>
                    <p>${transaction.amount} - ${transaction.category} - ${transaction.type}</p>
                    <p>${transaction.date} - ${transaction.description}</p>
                </div>
            `
        })
    })
}

function addTransaction(){
    const amount = document.getElementById('amount').value
    const category = document.getElementById('category').value
    const type = document.getElementById('type').value
    const date = document.getElementById('date').value
    const description = document.getElementById('description').value
    fetch('http://127.0.0.1:5000/transactions', {
        method: 'POST' ,
        headers: {'Content-Type': 'application/json'} ,
        body: JSON.stringify({amount, category, type, date, description})
    })
    
    .then(response => response.json())
    .then(() => {
        loadSummary()
        loadTransactions()
    })
}

loadSummary()
loadTransactions()