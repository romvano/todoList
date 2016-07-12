$( function() {
    $( 'form.js-delete' ).submit( function( e ) {
        e.preventDefault();
        var self = $( this );
        $.ajax( {
            url: '/list/delete/',
            type: 'post',
            data: $( this ).serialize(),
            success: function( resp ) {
                if( resp == 0 ) {
                    $( '.js-tr:eq(' + self.index( 'form.js-delete' ) + ')' ).hide();
                } else {
                    alert( resp );
                }
            },
            error: function( resp ) {
                if( resp == '<h1>403 Forbidden</h1>' ) {
                    alert( 'Incorrect user!' );
                }
            },
        } );
    } );
} );
