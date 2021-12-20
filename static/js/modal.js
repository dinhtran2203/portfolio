// Get the button that opens the modal
var modalBtn = document.getElementsByClassName('modalBtn')[0];
var modalBtn2 = document.getElementsByClassName('modalBtn')[1];

var modal = document.getElementsByClassName('modal')[0];
var modal2 = document.getElementsByClassName('modal')[1];

// Get the <span> element that closes the modal
var closeBtn = document.getElementsByClassName('closeBtn')[0];
var closeBtn2 = document.getElementsByClassName('closeBtn')[1];

// listen to event
// When the user clicks the button, open the modal 
modalBtn.addEventListener('click', openModal);
modalBtn2.addEventListener('click', openModal2);

closeBtn.addEventListener('click', closeModal);
closeBtn2.addEventListener('click', closeModal2);
// Outside click

window.addEventListener('click', clickOuside);


// create function for event
function openModal(){
  modal.style.display = 'block';
}

function openModal2(){
  modal2.style.display = 'block';
}

function closeModal(){
  modal.style.display = 'none';
}
function closeModal2(){
  modal2.style.display = 'none';
}

function clickOuside(e){
  if(e.target == modal ){
    modal.style.display = 'none';
  }
  
  if(e.target == modal2){
    modal2.style.display = 'none';
  }
}
