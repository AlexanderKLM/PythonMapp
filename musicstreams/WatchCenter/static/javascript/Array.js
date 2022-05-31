let users = ['Marks', 'James', 'Peter', 'Jane', 'Mary'];
function addLinks(){
    let template = users.map(user => `<li>${user}</li>`).join('\n');
    document.querySelector('ul').innerHTML = template;
    console.log(users)
}
addLinks();
let btnAdd = document.querySelector('button');
let input = document.querySelector('input');
btnAdd.addEventListener('click', () =>{
    users.push(input.value);
    input.value = '';
    addLinks();
});