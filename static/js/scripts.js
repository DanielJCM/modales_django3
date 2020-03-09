function abrir_modal(url)
{
        $('#popup').load(url, function()
        {
                $(this).modal('show');
        });
        return false;
}

function cerrar_modal()
{
        $('#popup').modal('hide');
        return false;
}

$(document).ready(function()
{
    var table = $('#tabla').dataTable( {
        "language": {
                url: "/static/localizacion/es_ES.json"
        }
    } );
});