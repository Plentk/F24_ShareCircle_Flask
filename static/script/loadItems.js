// loadItems.js is supposed to load items from a json file. Currently deprecated.
fetch("./shareCircleItems.json")
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    response.json()})
  .then(data => console.log(data))
  .catch(error => console.error('Failed to fetch data:', error));
