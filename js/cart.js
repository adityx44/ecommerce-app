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

let cart =
JSON.parse(localStorage.getItem("cart")) || [];

let html = "";

let total = 0;

cart.forEach(id => {

let product =
products.find(p => p.id === id);

html += `
<h3>${product.name}</h3>
<p>₹${product.price}</p>
`;

total += product.price;
});

html += `<h2>Total: ₹${total}</h2>`;

document.getElementById("cart").innerHTML =
html;