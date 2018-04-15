function acceptProposal(proposalID) {
    hideInfoProposal();
    var jqxhr = $.post( "/proposal", {type: 'accept',proposalID: proposalID}, function() {
        showInfoProposal("A sua acção foi registada")
        hideChangePropose()
    }).done(function() {

    })
    .fail(function(e) {
        showInfoProposal("Por favor, tente mais tarde")
    });
}


function rejectProposal(proposalID) {
    hideInfoProposal();
    var jqxhr = $.post( "/proposal", {type: 'reject',proposalID: proposalID}, function() {
       showInfoProposal("A sua acção foi registada")
       hideChangePropose()
    })
    .done(function() {

    })
    .fail(function(e) {
        showInfoProposal("Por favor, tente mais tarde")
    })

}

function showInfoProposal(msg) {
    $("#infoNewPropose").show();
    $("#infoNewProposemsg").text(msg)
}

function hideInfoProposal() {
    $("#infoNewPropose").hide();
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

function hideChangePropose() {
    $(".changeProposeStatus").hide()
}

$(document).ready(function () {
    hideInfoProposal();
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
