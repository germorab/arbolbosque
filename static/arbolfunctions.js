
var arbolfunctions = {
    
    texto : {
        
        guardar : function(){
            titulo = document.getElementById('textotitulo').value
            contenido = document.getElementById('textocontenido').value
            console.log("calling dj "+titulo+" " + contenido);
            //Dajaxice.src.apps.notification.rules_tab_single_event(Dajax.process, {"titulo":titulo , "contenido":contenido } );
            //Dajaxice.arbol.bosque.guardarTexto(Dajax.process );
            Dajaxice.arbol.bosque.guardarTexto(Dajax.process, {'titulo':titulo , 'contenido':contenido } );
        },
        
        test : function(){
            //Dajaxice.arbol.bosque.sayhello(my_js_callback);
            Dajaxice.arbol.bosque.sayhello(this.test2);
        },
        
        test2 : function (data){
            alert("called the other");
        }
        
    }
    
}

function my_js_callback(data){
    alert(data.message);
}

//Dajaxice.simple.my_function(callback, {'user': 'tom'}, {'error_callback': custom_error});
