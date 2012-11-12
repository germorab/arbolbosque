
var arbolfunctions = {
    
    texto : {
        guardar : function(){
            var titulo = document.getElementById('textotitulo').value
            var contenido = document.getElementById('textocontenido').value
            var categoria = document.getElementById('textolistacategorias').value
            
            if (titulo == ""){
                document.getElementById('resultado').innerHTML = "No se guardo nada. Titulo vacio";
                return;
            }
            Dajaxice.arbol.bosque.guardarTexto(Dajax.process, {'titulo':titulo , 'contenido':contenido, 'categoria' : categoria } );
        },
        
        setResultadoOK : function() {
            document.getElementById('resultado').innerHTML = "Contenido ingresado";
        }
    },
    
    categoria : {
        guardar : function(){
            var nombre = document.getElementById('categorianombre').value
            var descripcion = document.getElementById('categoriadesc').value
            
            if (nombre == ""){
                document.getElementById('resultado').innerHTML = "No se guardo nada. Titulo vacio";
                return;
            }
            Dajaxice.arbol.bosque.guardarCategoria(Dajax.process, {'nombre':nombre , 'descripcion':descripcion } );
        },
        
        setResultadoOK : function() {
            document.getElementById('resultado').innerHTML = "Categoria creada";
        }
    }
}
