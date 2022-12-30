const baseURL = 'http://' + window.location.host + '/api'
$('#warning').hide(); $('#success').hide(); $('#loading').hide();

function send(data) {
  axios.post(baseURL + '/registrations/', data)
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

document.getElementById('form-registration').addEventListener('submit', (event) => add(event))

  
function add(event) {
  event.preventDefault()

  $('#loading').show();

  let code = document.getElementById('code').value;
  let course = document.getElementById('course').value;
  let student = document.getElementById('student').value;

  const data = {
    code, course, student
  }

  send(data);
}

function del(id) {
  $('#warning').show().text('Deletando curso')
  axios.delete(baseURL + '/registrations/'+id)
    .then(response => {
      setTimeout(() => {
        window.location.reload()
      }, 500)
    })
    .catch(err => {
      console.log(err)
      let errors = err.response.data
      let keys = Object.keys(errors)
      $('#warning').show().text('Não foi possível deletar a matrícula')
    })
}
