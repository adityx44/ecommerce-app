const products = [
{
id:1,
name:"Laptop",
price:50000
},
{
id:2,
name:"Mouse",
price:500
},
{
id:3,
name:"Keyboard",
price:1500
}
];

let output = '<div class="product-container">';

products.forEach(product => {

output += `
<div class="card">
<h3>${product.name}</h3>
<p>₹${product.price}</p>

<button onclick="addToCart(${product.id})">
Add To Cart
</button>
</div>
`;

});

output += "</div>";

document.getElementById("products").innerHTML =
output;

function addToCart(id){

let cart =
JSON.parse(localStorage.getItem("cart")) || [];

cart.push(id);

localStorage.setItem(
"cart",
JSON.stringify(cart)
);

alert("Added To Cart");
}