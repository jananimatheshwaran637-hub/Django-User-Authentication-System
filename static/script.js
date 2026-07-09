document.querySelector("form").addEventListener("submit", function(){

    let username = document.querySelector(
        "input[name='username']"
    ).value;


    if(username==""){

        alert("Please enter username");

    }

});