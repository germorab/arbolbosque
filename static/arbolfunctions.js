
var arbolfunctions = {
    
    texto : {
        guardar : function(){
            titulo = document.getElementById('textotitulo').value
            contenido = document.getElementById('textocontenido').value
            categoria = document.getElementById('textolistacategorias').value
            if (titulo == ""){
                return;
            }
            Dajaxice.arbol.bosque.guardarTexto(Dajax.process, {'titulo':titulo , 'contenido':contenido, 'categoria' : categoria } );
        }
    },
    
    categoria : {
        guardar : function(){
            nombre = document.getElementById('categorianombre').value
            descripcion = document.getElementById('categoriadesc').value
            Dajaxice.arbol.bosque.guardarCategoria(Dajax.process, {'nombre':nombre , 'descripcion':descripcion } );
        }
    }
}



//Dajaxice.simple.my_function(callback, {'user': 'tom'}, {'error_callback': custom_error});
