
var arbolfunctions = {
    
    texto : {
        guardar : function(){
            titulo = document.getElementById('textotitulo').value
            contenido = document.getElementById('textocontenido').value
            //console.log("calling dj "+titulo+" " + contenido);
            Dajaxice.arbol.bosque.guardarTexto(Dajax.process, {'titulo':titulo , 'contenido':contenido } );
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
