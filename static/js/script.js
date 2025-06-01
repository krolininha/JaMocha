function validateEmail(event) {
    event.preventDefault();
    
    const emailInput = document.getElementById('emailInput');
    const emailMessage = document.getElementById('emailMessage');
    const subscribeBtn = document.getElementById('subscribeBtn');
    const email = emailInput.value;
    
    // Expressão regular para validação de email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // Remover classes anteriores
    emailInput.classList.remove('error', 'success');
    emailMessage.classList.remove('error-message', 'success-message');
    
    if (!email) {
        showMessage('Please enter your email address', 'error');
        return false;
    }
    
    if (!emailRegex.test(email)) {
        showMessage('Please enter a valid email address', 'error');
        return false;
    }
    
    // Email válido
    emailInput.classList.add('success');
    subscribeBtn.textContent = 'Subscribed!';
    showMessage('Thank you for subscribing to our newsletter!', 'success');
    
    // Reset após 3 segundos
    setTimeout(() => {
        emailInput.value = '';
        emailInput.classList.remove('success');
        emailMessage.textContent = '';
        subscribeBtn.textContent = 'Subscribe →';
    }, 3000);
    
    return false;
}

function showMessage(message, type) {
    const emailInput = document.getElementById('emailInput');
    const emailMessage = document.getElementById('emailMessage');
    
    emailInput.classList.add(type);
    emailMessage.textContent = message;
    emailMessage.classList.add(`${type}-message`);
    
    if (type === 'error') {
        emailInput.classList.add('shake');
        setTimeout(() => emailInput.classList.remove('shake'), 400);
    }
}