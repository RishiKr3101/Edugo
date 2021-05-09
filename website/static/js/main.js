const toggleButton = document.getElementsByClassName('toggle-button')[0]

const circle = document.getElementsByClassName('circle')[0]

const main_content = document.getElementsByClassName('main-content')[0]


const collapse_link = document.getElementsByClassName('collapse-link')[0]

toggleButton.addEventListener('click', () => {
    collapse_link.classList.toggle('active')
})

toggleButton.addEventListener('click', () => {
    circle.classList.toggle('active')
})

toggleButton.addEventListener('click', () => {
    main_content.classList.toggle('active')
})


function RemovePost(PostId){
    fetch('/remove-post',{
        method: "POST",
        body: JSON.stringify({ PostId: PostId}),
    }).then((_res) => {
        window.location.href = "/home";
    });
}