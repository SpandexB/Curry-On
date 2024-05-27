const apiUrl = "http://127.0.0.1:5001/recipe?ingredients=";
    const searchBox = document.querySelector(".search input");
    const searchBtn = document.querySelector(".gb");


    async function checkrecipe(ingreds) {
        const response = await fetch(apiUrl + ingreds);
        const data = await response.json();
    
        console.log(data);
    
    
        const recipe = data[0].recipe;
        const recipe1 = data[1].recipe;
        const recipe2 = data[2].recipe;

        let ingredients = data[0].ingredients;
        let ingredients1 = data[1].ingredients;
        let ingredients2 = data[2].ingredients;

        const score = data[0].score;
        const score1 = data[1].score;
        const score2 = data[2].score;

        const url = data[0].url;
        const url1 = data[1].url;
        const url2 = data[2].url;


    
    
      
        if (typeof ingredients === 'string') {
            try {
                ingredients = JSON.parse(ingredients);
            } catch (error) {
                console.error("Error parsing ingredients as JSON:", error);
                ingredients = [ingredients];
            }
        }

        if (typeof ingredients1 === 'string') {
            try {
                ingredients1 = JSON.parse(ingredients1);
            } catch (error) {
                console.error("Error parsing ingredients as JSON:", error);
                ingredients1 = [ingredients1];
            }
        }

        if (typeof ingredients2 === 'string') {
            try {
                ingredients2 = JSON.parse(ingredients2);
            } catch (error) {
                console.error("Error parsing ingredients as JSON:", error);
                ingredients2 = [ingredients2];
            }
        }









    
        if (Array.isArray(ingredients)) {
            ingredients = ingredients.map(ingredient => ingredient.trim());
        }

        if (Array.isArray(ingredients1)) {
            ingredients1 = ingredients1.map(ingredient => ingredient.trim());
        }
        if (Array.isArray(ingredients2)) {
            ingredients2 = ingredients2.map(ingredient => ingredient.trim());
        }











    
       
        document.querySelector(".rn0").innerHTML = recipe;
        document.querySelector(".rn1").innerHTML = recipe1;
        document.querySelector(".rn2").innerHTML = recipe2;




        const ingredientsList = document.querySelector(".ing0");
        ingredientsList.innerHTML = ""; 
        ingredients.forEach(ingredient => {
            const li = document.createElement("li");
            li.textContent = ingredient;
            ingredientsList.appendChild(li);
        });
        const ingredientsList1 = document.querySelector(".ing1");
        ingredientsList1.innerHTML = ""; 
        ingredients1.forEach(ingredient => {
            const li = document.createElement("li");
            li.textContent = ingredient;
            ingredientsList1.appendChild(li);
        });
        const ingredientsList2 = document.querySelector(".ing2");
        ingredientsList2.innerHTML = ""; 
        ingredients2.forEach(ingredient => {
            const li = document.createElement("li");
            li.textContent = ingredient;
            ingredientsList2.appendChild(li);
        });






        document.querySelector(".sc0").innerHTML = "Score : " + score;
        document.querySelector(".sc1").innerHTML = "Score : " + score1;
        document.querySelector(".sc2").innerHTML = "Score : " + score2;

        

        document.querySelector(".vrec0").href = url;
        document.querySelector(".vrec1").href = url1;
        document.querySelector(".vrec2").href = url2;
    

        document.querySelector(".recipes").style.display = "block";
        document.querySelector(".gnting").style.display = "none";
        searchBtn.classList.remove("shk");
        searchBtn.classList.add("animate");
        setTimeout(()=>{
            searchBtn.classList.remove("animate");
        },800);
    }
    
    
    
    
searchBtn.addEventListener("click", search);

document.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        search();
    }
});


    function search(){
        document.querySelector(".recipes").style.display = "none";
        checkrecipe(searchBox.value);




        var animationDiv = document.getElementById('gnting');
        animationDiv.style.display = 'block';
  
        document.querySelector(".gnting").style.display = "flex";
        


        searchBtn.classList.add("animate");
        searchBtn.classList.add("shk");

        setTimeout(()=>{
            searchBtn.classList.remove("animate");
        },800);
    }

    function goToHomepage(){
        window.location.href='homepage.html';
    }



