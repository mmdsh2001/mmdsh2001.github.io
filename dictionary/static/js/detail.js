const defLists = document.querySelectorAll('.def-list');

for (let index = 0; index < defLists.length; index++) {
    const defList = defLists[index];

    let items = defList.querySelectorAll("li");
    let totalItems = items.length;
    let visibleItems = 3;  // Set the initial number of visible items

    for (var i = visibleItems-1; i <totalItems ; i++) {
        items[i].classList.add('item-hiden');
    }

    // see more btn on click function
    let seeMore = defList.querySelector('.btn').onclick = function() {
   
    

        for (var i = visibleItems-1; i <totalItems ; i++) {
            items[i].classList.remove('item-hiden');
        }
        visibleItems = totalItems;
    
        if (visibleItems === totalItems) {
            this.style.display = "none";
        }
    
    }
    // don't show see more button if there is less than two items
    if(totalItems < 3){
        defList.querySelector(".btn").style.display = "none";
}

    

}

