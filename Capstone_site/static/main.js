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
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", height);
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", name);
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", bred_for);
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", breed_group);
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", life_span);
    document.querySelector('#pup-description').insertAdjacentHTML("beforeend", temperament);
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
   
    fillPupDescription(weight,height,name,bred_for,breed_group,life_span,temperament);
}

const changePup = () => {
    console.log(event.target.value)
    getPupByBreed(event.target.value)
    
}

fetchBreedPup();