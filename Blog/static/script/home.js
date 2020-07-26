// to show animation of blog list
function showAnimation(){
    document.getElementById('cardId').style.display='block'
}
// toggle list of profile drawer
function toggleImg(){
   var x = document.getElementById('profileId')
   if(x.style.display === 'block'){
    x.style.display='none'
   }
   else{
    x.style.display='block'
   }
}
// to show edit form of profile info
function enableProfileEdit(){
    var fieldObj = document.getElementById('profileFormId')
    var proList = document.getElementById('profileId')
    console.log(proList.style.display)
    if(proList.style.display === 'none'){
        fieldObj.style.display = 'none'
        proList.style.display ='block'
    }
    else{
        fieldObj.style.display = 'block'
        proList.style.display ='none'
    }
}
