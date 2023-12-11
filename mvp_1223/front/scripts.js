/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/pacientes';
    fetch(url, {
      method: 'get',
    })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.name, 
                                                item.age, 
                                                item.sex,
                                                item.cp,
                                                item.trestbps,
                                                item.chol,
                                                item.fbs,
                                                item.restecg,
                                                item.thalach,
                                                item.exang,
                                                item.oldpeak,
                                                item.slope,
                                                item.ca,
                                                item.thal,
                                                item.num
                                              ))          
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

function abrirCadastro(){
	$("#Sobra").css("display", "block");
}

function fecharCadastro(){
	$("#Sobra").css("display", "none");
}

/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputName, inputAge, inputSex,
                        inputCP, inputTrestbps, inputChol, 
                        inputFbs, inputRestecg, inputThalach,
                        inputExang, inputOldpeak, inputSlope,
                        inputCa, inputThal) => {
    
    const formData = new FormData();
    formData.append('name', inputName);
    formData.append('age', inputAge);
    formData.append('sex', inputSex);
    formData.append('cp', inputCP);
    formData.append('trestbps', inputTrestbps);
    formData.append('chol', inputChol);
    formData.append('fbs', inputFbs);
    formData.append('restecg', inputRestecg);
    formData.append('thalach', inputThalach);
    formData.append('exang', inputExang);
    formData.append('oldpeak', inputOldpeak);
    formData.append('slope', inputSlope);
    formData.append('ca', inputCa);
    formData.append('thal', inputThal);

    let url = 'http://127.0.0.1:5000/paciente';
    fetch(url, {
      method: 'post',
      body: formData
    })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
   let span = document.createElement("span");
   let txt = document.createTextNode("\u00D7");
   span.className = "close";
   span.appendChild(txt);
   parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
   let close = document.getElementsByClassName("close");
   // var table = document.getElementById('myTable');
   let i;
   for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
   }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
    console.log(item)
    let url = 'http://127.0.0.1:5000/paciente?name='+item;
    fetch(url, {
      method: 'delete'
    })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const novoCadastro = async () => {

    let inputName = document.getElementById("name").value;
    let inputAge = document.getElementById("age").value;
    let inputSex = document.getElementById("sex").value;
    let inputCp = document.getElementById("cp").value;
    let inputTrestbps = document.getElementById("trestbps").value;
    let inputChol = document.getElementById("chol").value;
    let inputFbs = document.getElementById("fbs").value;
    let inputRestecg = document.getElementById("restecg").value;
    let inputThalach = document.getElementById("thalach").value;
    let inputExang = document.getElementById("exang").value;
    let inputOldpeak = document.getElementById("oldpeak").value;
    let inputSlope = document.getElementById("slope").value;
    let inputCa = document.getElementById("ca").value;
    let inputThal = document.getElementById("thal").value;
    let inputNum = '';

    if (inputAge == '' || inputTrestbps  == '' || inputChol  == '' || inputThalach  == '' || inputOldpeak  == '' || inputSlope  == '' || inputCa  == '') {
      alert('Todos os campos é obrigatorio');
      callback();
    }

    // Verifique se o nome do produto já existe antes de adicionar
    const checkUrl = `http://127.0.0.1:5000/pacientes?nome=${inputName}`;
    fetch(checkUrl, {
      method: 'get'
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.pacientes && data.pacientes.some(item => item.name === inputName)) {
        alert("O paciente já está cadastrado.\nCadastre o paciente com um nome diferente ou atualize o existente.");
      } else if (inputName === '') {
        alert("O nome do paciente não pode ser vazio!");
      } else if (isNaN(inputAge) || isNaN(inputTrestbps) || isNaN(inputChol) || isNaN(inputThalach) || isNaN(inputOldpeak) || isNaN(inputSlope) || isNaN(inputCa)) {
        alert("Esse(s) campo(s) precisam ser números!");
      } else {
        insertList(inputName, inputAge, inputSex, inputCp, inputTrestbps, inputChol, inputFbs, inputRestecg, inputThalach, inputExang, inputOldpeak, inputSlope, inputCa, inputThal, inputNum);
        postItem(inputName, inputAge, inputSex, inputCp, inputTrestbps, inputChol, inputFbs, inputRestecg, inputThalach, inputExang, inputOldpeak, inputSlope, inputCa, inputThal);
        alert("Item adicionado!");
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (inputName, inputAge, inputSex, inputCp, inputTrestbps, inputChol, inputFbs, inputRestecg, inputThalach, inputExang, inputOldpeak, inputSlope, inputCa, inputThal, inputNum) => {
  
  var resultado = '';
  var sexo = '';
  var acucar = '';
  var eletroc = '';

  if(inputSex == 0){sexo = 'Mulher';}else{sexo = 'Homem'}
  if(inputNum == 0){resultado = 'Não há doença cardíaca';}else{resultado = 'Há doença cardíaca';}
  if(inputFbs == 0){acucar = 'Não';}else{acucar = 'Sim';}
  if(inputRestecg == 0){eletroc = 'Normal';}else if(inputRestecg == 1){eletroc = 'Anormalidades de ST-T';}else{eletroc = 'Hipertrofia ventricular';}

  var item = [inputName, inputAge, sexo, inputTrestbps, inputChol, acucar, eletroc, inputThalach, resultado];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("name").value = "";
  document.getElementById("age").value = "";
  document.getElementById("sex").value = "";
  document.getElementById("cp").value = "";
  document.getElementById("trestbps").value = "";
  document.getElementById("chol").value = "";
  document.getElementById("fbs").value = "";
  document.getElementById("restecg").value = "";
  document.getElementById("thalach").value = "";
  document.getElementById("exang").value = "";
  document.getElementById("oldpeak").value = "";
  document.getElementById("slope").value = "";
  document.getElementById("ca").value = "";
  document.getElementById("thal").value = "";

  removeElement();
}


