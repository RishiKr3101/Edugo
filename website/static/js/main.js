const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbar = document.getElementsByClassName('navbar-links')[0]
const circle = document.getElementsByClassName('circle')[0]

const collapse_link = document.getElementsByClassName('collapse-link')[0]

toggleButton.addEventListener('click', () => {
    collapse_link.classList.toggle('active')
})

toggleButton.addEventListener('click', () => {
    circle.classList.toggle('active')
})