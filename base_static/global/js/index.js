function alertaExcluir(){
    const btnExluir = document.querySelectorAll(".btn-excluir");
    for(let btn of btnExluir){
        btn.addEventListener('click', (event) => {
            event.preventDefault();
            const confirmar = confirm("Você tem certeza que deseja remover esta tarefa ?")
            if(confirmar)
        });
    }
}

function eventoSair(){
    const formLogout = document.querySelector(".form-logout");
    formLogout.addEventListener('submit',(e) => {
        e.preventDefault();
        formLogout.submit();
    });
}


eventoSair();
alertaExcluir();
