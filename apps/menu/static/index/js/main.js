/*$( document ).ready(function() {
    // Handler for .ready() called.
    alert('Todo bien');
  });*/

function editarDocente(dni, legajo, nombre, apellido, correo, carrera, estado, sexo) {
    console.log("Editando");
    document.getElementById("dni_editar").value = dni;
    document.getElementById("nombre_editar").value = nombre;
    document.getElementById("apellido_editar").value = apellido;
    document.getElementById("correo_editar").value = correo;
    document.getElementById("estado_editar").checked = estado;
    document.getElementById("sexo_editar").value = sexo;
    console.log(dni);
    // mostrar notificacion con dni
    alert('Editando Docente: ' + dni + ', Al finalizar la edición se creará un nuevo registro con los datos editados');
}

  function eliminarDocente(dni) {
    document.getElementById("dni_docente").value = dni;
    console.log("Eliminado");
    console.log(dni);
}

function editarEstudiante(dni, legajo, nombre, apellido, correo, carrera, estado, sexo) {
    console.log("Editando");
    document.getElementById("dni_editar").value = dni;
    document.getElementById("legajo_editar").value = legajo;
    document.getElementById("nombre_editar").value = nombre;
    document.getElementById("apellido_editar").value = apellido;
    document.getElementById("correo_editar").value = correo;
    document.getElementById("carrera_editar").value = carrera;
    document.getElementById("estado_editar").checked = estado;
    document.getElementById("sexo_editar").value = sexo;
    console.log(dni);
    // mostrar notificacion con dni
    alert('Editando Estudiante: ' + dni + ', Al finalizar la edición se creará un nuevo registro con los datos editados');
}

function eliminarEstudiante(dni) {
  document.getElementById("legajo_estudiante").value = dni;
  console.log("Eliminado");
  console.log(dni);
}

function editarMateria(codigo, nombre, descripcion,docente, estado ) {
  console.log("Editando");
  document.getElementById("codigo_editar").value = codigo;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("docente_editar").value = docente;
  document.getElementById("estado_editar").value = estado;
  console.log(codigo);
  // mostrar notificacion con codigo
  alert('Editando Materia: ' + codigo + ' , Al finalizar edicion se creara un nuevo registro con los datos editados');
}

function editarCarrera(codigo, nombre, descripcion,duracion, estado ) {
  console.log("Editando");
  document.getElementById("codigo_editar").value = codigo;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("duracion_editar").value = duracion;
  document.getElementById("estado_editar").value = estado;
  console.log(codigo);
  // mostrar notificacion con codigo
  alert('Editando Carrera: ' + codigo + ' , Al finalizar edicion se creara un nuevo registro con los datos editados');
}

function eliminarCarrera(codigo) {
  document.getElementById("id_carrera").value = codigo;
  console.log("Eliminado");
  console.log(codigo);
}

function eliminarMateria(codigo) {
  document.getElementById("id_materia").value = codigo;
  console.log("Eliminado");
  console.log(codigo);
}

function borrarContent(){
  document.getElementById("search").value = "";
}



function activarEspera(){
  const btn = document.getElementById("btn");
  btn.innerHTML = 'Generando ... <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
  btn.disabled = true;
}

$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 