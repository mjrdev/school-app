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
