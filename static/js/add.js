$( function() {
    $( 'form.js-add' ).submit( function( e ) {
        e.preventDefault();
    } );
    $( '.js-add_text:eq( 0 )' ).keypress( function( args ) {
        var self = $( this );
        if( args.which == 13 && $( '.js-add_text:eq( 0 )' ).val() != '' && $( '.js-datepicker:eq( 0 )' ).val().match( /^(\d{4})\/(\d{2})\/(\d{2}) (\d{2}):(\d{2})$/ ) ) {
            $.ajax( {
                url: '/list/add/',
                type: 'post',
                data: $( 'form.js-add:eq( 0 )' ).serialize(),
                success: function( response ) {
                    resp = JSON.parse( response );
                    if( resp[ 'code' ] == 0 ) {
                        $( '.js-table:eq( 0 )' ).prepend(                            
                                      '<tr class="js-tr"><td class="col-md-1"><form method="POST" class="js-do_undo" action="/list/do_undo-nojs/"><input type="hidden" name="pk" value="' +resp['pk']+'" /><input type="checkbox" name="done" class="form-control js-do_undo" /></form></td>' +
                                      '<td class="col-md-3 td-padding"><p class="note-added js-note_deadline">' + resp[ 'deadline' ] + '</p></td>' +
                                      '<td class="col-md-7 td-padding"><p class="note-added js-note_text">' + resp[ 'text' ] + '</p></td>' +
                                      '<td class="col-md-1 td"><form method="POST" action="list/delete-nojs/" class="js-delete"><input type="hidden" name="pk" value="' + resp[ 'pk' ] + '" /><input type="submit" class="form-control" value="Delete" /></form></td>'                   
                            );
                        $.getScript( 'static/js/do_undo.js' );
                        $.getScript( 'static/js/delete.js' );
                        $( '.js-add_text' ).val( '' );
                    } else {
                        alert( response );
                    }
                },
                // TODO
                error: function( resp ) {
                        alert( 'Incorrect user!' );
                },
            } );
        }
    } );
} );
