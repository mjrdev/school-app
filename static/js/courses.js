const baseURL = 'http://' + window.location.host + '/api'

$('#warning').hide(); $('#success').hide(); $('#loading').hide();

function send(data) {
  axios.post(baseURL + '/courses/', data)
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
      $('#warning').show().text('Preencha todos os campos por favor!')
    })
  
    $('#loading').hide();
}

document.getElementById('form-course').addEventListener('submit', (event) => add(event))

  
function add(event) {
  event.preventDefault()

  $('#loading').show();

  let title = document.getElementById('title').value;
  let description = document.getElementById('description').value;
  let teacher = document.getElementById('teacher').value;
  let shift = document.getElementById('shift').value;

  const data = {
    title: title,
    description: description,
    shift: shift,
    teacher: teacher
  }

  send(data);
}

function del(id) {
  $('#warning').show().text('Deletando curso')
  axios.delete(baseURL + '/courses/'+id)
    .then(response => {
      setTimeout(() => {
        window.location.reload()
      }, 500)
    })
    .catch(err => {
      console.log(err)
      let errors = err.response.data
      let keys = Object.keys(errors)
      $('#warning').show().text('Preencha todos os campos por favor!')
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
