const updateButton = document.getElementsByClassName("update-basket");

for (let i = 0; i < updateButton.length; i++) {
  updateButton[i].addEventListener("click", function () {
    let productId = this.dataset.product;
    let action = this.dataset.action;

    console.log(productId, action);

    console.log(user);
    if (user === "AnonymousUser") {
      console.log("not logged in");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is logged in sending data...");

  const url = "update_item/";

  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data: ", data);
    });
}
