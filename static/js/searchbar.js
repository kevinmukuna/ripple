// get all the post
const postLists = document.querySelector("#all_posts");
// get section in which result output will be displayed
const searchPostsOutput = document.querySelector("#search_posts_output");
searchPostsOutput.style.display = "none";
// // get access the search bar
const searchBar = document.querySelector("#searchBar");
// add an event listner on key up
searchBar.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    // trim removes empty spaces
    if (searchValue.trim().length > 0) {
        // reset the result fro each search
        searchPostsOutput.innerHTML = "";
        // fetch the data from the db
        fetch("/search_posts", {
            body: JSON.stringify({ searchText: searchValue }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                // display the data and hide some section based on the conditions
                console.log("data", data);
                postLists.style.display = "none";
                searchPostsOutput.style.display="block";
                if (data.length === 0) {
                    searchPostsOutput.innerHTML ="no results found"
                }
                else {
                    // display result
                    data.forEach( post => {
                       searchPostsOutput.innerHTML+=`
                        <article class="media content-section">
                            <img class="rounded-circle article-img" src="${post.author_id}">
                            <div class="media-body w-50">
                                <div class="article-metadata row ml-1 pb-2">
                                    <a class="mr-2 " href="">${post.author}</a>
                                    <small class="text-muted my-auto">${post.date_posted}</small>
                                </div>
                                <h2><a class="article-title" href="">${post.title }</a></h2>
                                <p class="article-content">${post.address_line_1}, ${post.address_line_2}, ${post.city},
                                        ${post.county}</p>
                                <ul id="lightSlider" class="gallery list-unstyled cS-hidden">
                                       <li>
<!--                                            <img src=""/>-->
                                       </li>
                                </ul>

                                <p class="article-content">${ post.property_description}</p>

                                `
                    });
                }
            });
    } else {
        searchPostsOutput.style.display="none";
        postLists.style.display="block";
    }
});