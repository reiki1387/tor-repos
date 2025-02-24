document.getElementById('alertBtn').addEventListener('click', function() {
    alert('Hello from ME, you and JavaScript!');
});

document.getElementById('alertBtn2').addEventListener('click', function() {
    alert('Buttion 2 CLicked!');
});

document.getElementById('alertBtn3').addEventListener('click', function() {
    alert('Button 3 Clicked!');
});

document.getElementById('goToPage2Btn').addEventListener('click', function() {
    window.location.href = '/page_2';
});

document.getElementById('goBackBtn').addEventListener('click', function() {
    alert('go back btn Clicked!')
    window.location.href = '/';
});