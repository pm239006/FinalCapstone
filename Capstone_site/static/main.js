const BASE_API_URL = 'https://api.thedogapi.com/v1'

const fetchBreedPup = async () => {

    const response = await fetch( BASE_API_URL + '/breeds')
    const pupBreeds = await response.json();
    populatePupSelect(pupBreeds);
}

const populatePupSelect = (breeds) => {
    const select = document.querySelector('.breed-select');
    const breedOptions = breeds.map(breed => {
        const option = document.createElement('option');
        option.text = breed.name;
        option.value = breed.id;
       
        return option
    })

    breedOptions.forEach(breedOption => {
        select.appendChild(breedOption);
        })

}

const fillPupImage = (imageUrl) => {
    document.querySelector('#pupImage').setAttribute('src', imageUrl);
}

// const fillPupWeight = (weight) => {
//     document.querySelector('#pup-weight').setAttribute('src', weight);

// }

const fillPupDescription = (weight,height,name,bred_for,breed_group,life_span,temperament) => {
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", weight);
    document.querySelector('#pup-height').insertAdjacentHTML("beforeend", height);
    document.querySelector('#pup-name').insertAdjacentHTML("beforeend", name);
    document.querySelector('#pup-bred_for').insertAdjacentHTML("beforeend", bred_for);
    document.querySelector('#pup-breed_group').insertAdjacentHTML("beforeend", breed_group);
    document.querySelector('#pup-life_span').insertAdjacentHTML("beforeend", life_span);
    document.querySelector('#pup-temperament').insertAdjacentHTML("beforeend", temperament);
}

const fillPupWeight= (weight) => {
    document.querySelector('#pup-weight').insertAdjacentHTML("beforeend", weight)
}

const fillPupHeight = (height) => {
    document.querySelector('#pup-height').insertAdjacentHTML("beforeend", height)
}
const fillPupName = (name) => {
    document.querySelector('#pup-name').insertAdjacentHTML("beforeend", name)
}

const fillPupBred_For = (bred_for) => {
    document.querySelector('#pup-bred_for').insertAdjacentHTML("beforeend", bred_for)
}
const fillPupBreed_Group = (breed_group) => {
    document.querySelector('#pup-breed_group').insertAdjacentHTML("beforeend", breed_group)
}

const fillPupLife_Span = (life_span) => {
    document.querySelector('#pup-life_span').insertAdjacentHTML("beforeend", life_span)
}

const fillPupTemperament = (temperament)=> {
    document.querySelector('#pup-temperament').insertAdjacentHTML("beforeend", temperament)
}


const getPupByBreed = async (breedId) => {
    const [data] = await fetch(BASE_API_URL + '/images/search?include_breed=1&breed_id=' + breedId).then((data) => data.json())
    const {url: imageUrl} = data;
    const data2 = await fetch(BASE_API_URL + '/breeds/' + breedId)
    const breedInfo = await data2.json()
    const {name:name, bred_for:bred_for,breed_group:breed_group,life_span:life_span,temperament:temperament} = breedInfo
    const weight = breedInfo.weight.imperial
    const height = breedInfo.height.imperial

    fillPupImage(imageUrl);
    fillPupWeight(weight);
    fillPupHeight(height);
    fillPupName(name);
    fillPupBred_For(bred_for);
    fillPupBreed_Group(breed_group);
    fillPupLife_Span(life_span);
    fillPupTemperament(temperament);
}


const changePup = () => {
    console.log(event.target.value)
    getPupByBreed(event.target.value)
    
}

fetchBreedPup();