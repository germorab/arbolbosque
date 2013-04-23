
var arbolfunctions = {
    
    
    indice : {
        categoria : function (){

            Dajaxice.arbol.bosque.mostrarDialogoCategoria(Dajax.process);
        
        },
        
        diag_close : function() {
            $("#dialog-confirm").dialog('destroy');
            $("#dialog-confirm").remove();
            
        },

        diag : function(diagvars) {

            $("#dialog-confirm").dialog(
                    {modal:true},
                    {resizable: false},
                    {width: diagvars[0]},
                    {height: diagvars[1]},
                    {close:function(){arbolfunctions.indice.diag_close(); }}
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
