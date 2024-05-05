class WordCount {
  /*
  Contar cuantas veces aparece cada palabra en un subtitulo(ASCII)
  En ingles algunas contracciones se consideran como una palabra como we're
  Simbolo que no separa las palabras es el apostrofe
  Los numeros se consideran palabras

  "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.
  The mapping for this subtitle would be:
  textCopy code123: 1
  agent: 1
  cried: 1
  fled: 1
  i: 1
  password: 2
  so: 1
  special: 1
  that's: 1
  the: 2
  ***Este resultado es parecido a un Map<String, int> : Map<palabra, cantidad>

  */

  Map<String, int> countWords(String subtitle) {
    //Para el lado de String en minusculas
    subtitle = subtitle.toLowerCase();
    //Metodo Regexp para eliminar signos excepto apóstrofe y espacios
    //replaceAll(Pattern from, String replace)
    //Eliminar todo caracter que no sea alfanumerico, espacios o apostrofe como ! , .
    String cleanSubtitle = subtitle.replaceAll(RegExp(r"[^\w\s']"), '');
    //Dividir subtitle en palabras y conservarlo en una lista
    List<String> words = cleanSubtitle.split(RegExp(r'\s+'));
    //Almacenar frecuencia de palabras en variable wordCount
    Map<String, int> wordCount = {};

    //Contador
    for (String word in words) {
      //i=0 = 'word' ...
      if (word.isNotEmpty) {
        //En la lista wordCount se almacena el primer string
        //"hello" : hello está en la lista? Si +1 No 0
        //hello : 0
        wordCount[word] = (wordCount[word] ?? 0) + 1;
      }
    }
    return wordCount;
  }
}
