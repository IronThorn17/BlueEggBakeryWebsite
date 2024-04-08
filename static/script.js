document.addEventListener('DOMContentLoaded', function() {
    const productIdInput = document.getElementById('productId');
    const quantityInput = document.getElementById('quantity');
    const decrementButton = document.querySelector('.decrement');
    const incrementButton = document.querySelector('.increment');
    const addToCartButton = document.querySelector('.add-to-cart');

    // Set default value of quantity input to 0
    quantityInput.value = 0;

    decrementButton.addEventListener('click', function() {
        const currentValue = parseInt(quantityInput.value);
        if (currentValue > 0) {
            quantityInput.value = currentValue - 1;
        }

        console.log(quantityInput.value);
    });

    incrementButton.addEventListener('click', function() {
        const currentValue = parseInt(quantityInput.value);
        quantityInput.value = currentValue + 1;

        console.log(quantityInput.value);
    });

    addToCartButton.addEventListener('click', function(event) {
        // Prevent the default form submission
        event.preventDefault();
        
        // Retrieve the product ID and quantity values
        const productId = parseInt(productIdInput.value);
        const quantity = parseInt(quantityInput.value);
        
        // Perform any additional actions with the quantity value, such as adding the product to the cart
        if (quantity >= 1) {
            // Send data to server for adding to cart
            // Perform an AJAX request to the server to add the product to the cart
            fetch('/add-to-cart', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    product_id: productId,
                    quantity: quantity
                })
            })
            .then(response => response.json())
            .then(data => {
                // Log the response message
                console.log(data.message);
            })
            .catch(error => {
                // Log any errors that occur during the request
                console.error('Error:', error);
            });
            console.log('Product added to cart:', quantity);
        }
    });
});
