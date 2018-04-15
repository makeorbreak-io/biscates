function acceptProposal(proposalID) {
    var jqxhr = $.post( "/proposal", {type: 'accept',proposalID: proposalID}, function(result) {
        alert( result );
    })
    .done(function() {
        alert( "second success" );
    })
    .fail(function() {
        alert( e.toString() );
    })
    .always(function() {
        alert( "finished" );
    });
}

function rejectProposal(proposalID) {
    var jqxhr = $.post( "/proposal", {type: 'reject',proposalID: proposalID}, function() {
        alert( "success" );
    })
    .done(function() {
        alert( "second success" );
    })
    .fail(function(e) {
        alert( e.toString() );
    })
    .always(function() {
        alert( "finished" );
    });
}

function rate(rate, from_user, to_user, task_id) {
    var jqxhr = $.post( "/rate", {rate: rate, from_user: from_user, to_user: to_user, task_id: task_id}, function() {
    })
        .done(function() {
        })
        .fail(function(e) {
        })
        .always(function() {
        });
}

$(document).ready(function () {
  $('.ui.rating').rating('setting', 'onRate', function(value) {
    from_user = $('.rating').data('from');
    to_user = $('.rating').data('to');
    task_id = $('.rating').data('id');

    rate(value, from_user, to_user, task_id);
  });

  $('.ui.dropdown').dropdown({
      onChange: function(){
          $('.create-task > input').removeAttr('disabled');
      }
  });
});
