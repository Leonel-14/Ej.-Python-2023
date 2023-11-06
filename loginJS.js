function entrar(){

    var usuario = document.getElementById("username").value;
    var correos = ["leo1@gmail.com","leo2@gmail.com","leo3@gmail.com","leo4@gmail.com"];
    var bool = false
    for(let i = 0; i<correos.length; i++)
    {
        if(usuario == correos[i])
        {
            bool = true;
            break;
        }
    }

    if(bool == true)
    {
        alert("Usuario Encontrado");
        
    }
    else
    {
        alert("Usuario no Existe");
        
    }

}