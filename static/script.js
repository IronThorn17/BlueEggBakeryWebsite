document.addEventListener('DOMContentLoaded', function() {
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
        
        // Retrieve the quantity value when the "Add to Cart" button is clicked
        const quantity = parseInt(quantityInput.value);
        
        // Perform any additional actions with the quantity value, such as adding the product to the cart
        if (quantity >= 1) {
            // Send data to server for adding to cart
            // For now, you can log a message indicating the product and quantity added to the cart
            console.log('Product added to cart:', quantity);
        }
    });
});
