const tabs = document.getElementsByClassName('tab-content')
const sliderLower = document.getElementById('slider-lower')
const sliderUpper = document.getElementById('slider-upper')
const minPrice =document.getElementById('min')
const maxPrice = document.getElementById('max')


for( let i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener('click', () => {
        console.log(tabs[i], )
        for (let j = 0; j < tabs.length; j++) {
            tabs[j].classList.remove('active')
            tabs[j].children[0].classList.remove('active')
            tabs[j].children[1].classList.remove('active')
        }

        tabs[i].classList.add('active')
        tabs[i].children[0].classList.add('active')
        tabs[i].children[1].classList.add('active')

    })
}

sliderLower.addEventListener('input', () => sliderChange());
sliderUpper.addEventListener('input', () => sliderChange());


function sliderChange() {
    console.log('sliding')
    const lowerValue = sliderLower.value;
            const upperValue = sliderUpper.value;

            if (parseInt(lowerValue) > parseInt(upperValue)) {
                sliderLower.value = upperValue;
            }

            minPrice.value = sliderLower.value
            maxPrice.value = sliderUpper.value
    console.log(sliderLower.value, sliderUpper.value)
}

