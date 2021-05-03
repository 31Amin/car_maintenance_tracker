$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".remove_item").hide();
    $(".record_error_car").hide();
    $(".record_error_garage").hide();
    $('.tooltipped').tooltip();
    $('.modal').modal();
    $('.datepicker').datepicker({
         format: "dd, mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "select"
        }
    });

    $(".chevron").click(function(){
        $(".chevron_icon").toggleClass("fa-chevron-up");
        $(".chevron_icon").toggleClass("fa-chevron-down");
    });
   
    
    });

// Add / remove lines to service item list in add_record task.
$(".add_item").click(function () {
    $(".item").append(' <input placeholder="Add service line item" id="service_items" name="service_items" type="text" class="validate addtional_line"><label for="serviceservice_items_cost"></label> ');
    $(".remove_item").show();
    });

$(".remove_item").click(function () {
    $(".addtional_line").last().remove();
    });

$(".remove_item_edit").click(function () {
    $(".addtional_line").last().remove();
    });

// Error message for user if garage or car not selected
$(".record_submit").click(function() {
    let selected_car = $( "#reg_no" ).val();
    let selected_gar = $( "#garage_name" ).val();
    if (selected_car == null){
        $(".record_error_car").show();
    }
    else if (selected_gar == null){
        $(".record_error_garage").show();
    }
})

$(".select_car").change(function() {
    $(".record_error_car").hide();
})
$(".select_garage").change(function() {
    $(".record_error_garage").hide();
})