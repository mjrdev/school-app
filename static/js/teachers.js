const baseURL = 'http://' + window.location.host + '/api'

$('#warning').hide(); $('#success').hide(); $('#loading').hide();

function send(data) {
  axios.post(baseURL + '/teachers/', data)
    .then(response => {
      $('#success').show()
      setTimeout(() => {
        window.location.reload()
      }, 2000)
    })
    .catch(err => {
      let errors = err.response.data
      let keys = Object.keys(errors)
      $('#warning').show().text('Preencha todos os campos por favor!')
    })
  
    $('#loading').hide();
}

document.getElementById('form-teacher').addEventListener('submit', (event) => add(event))

  
function add(event) {
  event.preventDefault()

  $('#loading').show();

  let name = document.getElementById('name').value;
  let cpf = document.getElementById('cpf').value;
  let email = document.getElementById('email').value;
  let about = document.getElementById('about').value;
  let password = document.getElementById('password').value;

  const data = {
    name,
    cpf,
    email,
    about,
    password
  }

  if (cpf.length != 11) {
    $('#warning').show().text('CPF inválido')
    return
  }

  send(data);
}

function del(id) {
  $('#warning').show().text('Deletando curso')
  axios.delete(baseURL + '/teachers/'+id)
    .then(response => {
      setTimeout(() => {
        window.location.reload()
      }, 500)
    })
    .catch(err => {
      console.log(err)
      let errors = err.response.data
      let keys = Object.keys(errors)
      $('#warning').show().text('Não foi possível deletar, esse Professor deve está vinculado a algum curso.')
    })
}

function search(str) {
  const items = document.getElementsByClassName('item')

  for (let item of items) {
    let searchAt = item.getElementsByTagName('span')[0].innerHTML.toLowerCase().indexOf(str);
    if (searchAt != -1) {
      item.style.setProperty('display', 'flex', 'important')
    } else {
      item.style.setProperty('display', 'none', 'important')
    }

    if (str.length == 0) {
      item.style.setProperty('display', 'flex', 'important')
    }
  }
}

document.getElementById('search')
  .addEventListener('input', () => {
  let str = document.getElementById('search').value.toLowerCase()
  search(str)
})
