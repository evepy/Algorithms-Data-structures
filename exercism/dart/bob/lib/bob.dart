class Bob {
  //condición ? valor_si_verdadero : valor_si_falso
 String response(String respuesta) =>
  respuesta == respuesta.toUpperCase() ? 'Whoa, chill out'
  : respuesta.endsWith("?") ? 'Sure'
  : respuesta == respuesta.toUpperCase() && respuesta.endsWith("?") ? "Calm down, I know what I'm doing!"
  : respuesta.isEmpty ? 'Fine. Be that way!'
  : 'Whatever.';
}
