document.addEventListener('DOMContentLoaded', () => {
    // Making enter key to submit the page 
    let msg = document.querySelector('#user_message');
    msg.addEventListener('key-up', event => {
        event.preventDefault();
        if (event.keyCode==13) {
            document.querySelector('#send_message').click();

        }
    })
})