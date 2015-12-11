
var arbolfunctions = {


    indice : {
        categoria : function (){
            Dajaxice.arbol.bosque.mostrarDialogoCategoria(Dajax.process);
        },
        
        texto : function (){
            Dajaxice.arbol.bosque.mostrarDialogoTexto(Dajax.process);
        },
        
        busqueda : function (){
            Dajaxice.arbol.bosque.mostrarDialogoBusqueda(Dajax.process);
        },
        
        imagen : function (){
            Dajaxice.arbol.bosque.mostrarDialogoImagen(Dajax.process);
        },
        
        pagina : function (){
            Dajaxice.arbol.bosque.mostrarDialogoPagina(Dajax.process);
        },
        
        diag_close : function() {
            $("#dialog-confirm").remove();
            $("#dialog-confirm").dialog('destroy');
            $("#textolistacategorias").dialog('destroy');
        },

        diag : function(diagvars) {
            
            $("#dialog-confirm").dialog(
                {modal:true},
                {title:"Arquitectura de la Informacion en un Entorno 3D para Wikipedia"},
                {resizable: false},
                {width: "40%"},
                {height: "auto"},
                {close:function(){$(this).dialog("close"); }}
            );
        }
    },
    
    texto : {
        guardar : function(){
            var titulo = document.getElementById('textotitulo').value;
            var contenido = document.getElementById('textocontenido').value;
            var categoria = $("#textolistacategorias").val();
            
            document.getElementById('resultado').innerHTML = "Trabajando";
            
            if (titulo == ""){
                document.getElementById('resultado').innerHTML = "Por favor ingrese un titulo";
                return;
            }
            
            if (categoria == null){
                document.getElementById('resultado').innerHTML = "Por favor seleccione una o más categorías";
                return;
            }
            
            Dajaxice.arbol.bosque.guardarTexto(Dajax.process, {'titulo':titulo , 'contenido':contenido, 'categoria' : categoria } );
        },
        
        setResultadoOK : function() {
            document.getElementById('resultado').innerHTML = "Contenido ingresado";
        },
        
        setResultadoError : function() {
            document.getElementById('resultado').innerHTML = "Ocurrió un error. Intente de nuevo";
        }
    },
    
    categoria : {
        guardar : function(){
            var nombre = document.getElementById('categorianombre').value;
            var descripcion = document.getElementById('categoriadesc').value;
            
            document.getElementById('resultado').innerHTML = "Trabajando";
            
            if (nombre == ""){
                document.getElementById('resultado').innerHTML = "Por favor ingrese un nombre";
                return;
            }
            Dajaxice.arbol.bosque.guardarCategoria(Dajax.process, {'nombre':nombre , 'descripcion':descripcion } );
        },
        
        setResultadoOK : function() {
            document.getElementById('resultado').innerHTML = "Categoría creada";
        }
    }
    
    
    
}
