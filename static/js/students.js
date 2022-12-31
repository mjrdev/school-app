const baseURL = 'http://' + window.location.host + '/api'
$('#warning').hide(); $('#success').hide(); $('#loading').hide();

document.cookie = 'csrf-token: ' + document.getElementsByName("csrfmiddlewaretoken")[0].value
const token = document.getElementsByName("csrfmiddlewaretoken")[0].value


const config = {     
  headers: {
    'content-type': 'application/json',
    'X-CSRF-TOKEN': document.getElementsByName("csrfmiddlewaretoken")[0].value,
  },
  withCredentials: true,
}

function send(data) {
  axios.post(baseURL + '/students/', data, config)
    .then(response => {
      $('#success').show()
      setTimeout(() => {
        window.location.reload()
      }, 2000)
    })
    .catch(err => {
      console.log(err)
      let errors = err.response.data
      let keys = Object.keys(errors)
      $('#warning').show().text('Preencha todos os campos corretamente por favor!')
    })
  
    $('#loading').hide();
}

document.getElementById('form-student').addEventListener('submit', (event) => add(event))

  
function add(event) {
  event.preventDefault()

  $('#loading').show();

  let name = document.getElementById('name').value;
  let cpf = document.getElementById('cpf').value;
  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;

  if (cpf.length != 11) {
    $('#warning').show().text('CPF inválido')
    return
  }

  const data = {
    name,
    cpf,
    email,
    password,
    token
  }

  console.log(password)

  send(data);
}

function del(id) {
  $('#warning').show().text('Deletando curso')
  axios.delete(baseURL + '/students/'+id)
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
