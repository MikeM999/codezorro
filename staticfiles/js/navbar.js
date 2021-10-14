<script src="https://js.stripe.com/v3/"></script>
<script>
    var stripe = Stripe('{{ stripe_public_key }}');
    const donate_button = document.querySelector('#donate_button')
    donate_button.addEventListener('click',event => {
        stripe.redirectToCheckout({
        sessionId: '{{ session_id }}'
    }).then(function(result) {});
    })
</script>