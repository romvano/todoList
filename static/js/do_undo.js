$( function() {
    $( 'form.js-do_undo' ).submit( function( e ) {
        e.preventDefault();
    } );
    $( "input.js-do_undo" ).on( "change", function() {
        $.ajax( {
            url: '/list/do_undo/',
            type: 'post',
            data: $( this ).parent().serialize(),
            success: function( resp ) {
                if( resp == 0 ) {
                    $( this ).parent().children( '.js-note' ).toggleClass( 'note-done' );
                }
            },
        } );
    } );
} );
