<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'
const users = ref([]);
const config = useRuntimeConfig()
const router = useRouter()
const idUsuario = router.currentRoute.value.query.idUsuario

let data, pending, error;
let item;
if(idUsuario!==undefined)
{
    ({ data, pending, error } = await useFetch(
    `${config.public.apiBase}/api/users/${idUsuario}/`,
    { method: 'GET' }))

    item = data.value;
}

const listFields = [
    {
        propName: "fullname",
        fieldName: "Nome *",
    },
    {
        propName: "email",
        fieldName: "E-mail *",
    },
    {
        propName: "adress",
        fieldName: "Endereço *",
    },
    {
        propName: "phone",
        fieldName: "Telefone *",
    },
]

async function Voltar(){
    navigateTo('/usuarios')
}

async function Salvar(params){
    let method = (idUsuario !== null && idUsuario !== undefined) ? "PUT" : "POST";
    let { data, error } = await useFetch(
    `${config.public.apiBase}/api/users/${(method == 'PUT' ? idUsuario + '/' : '')}`,
    { 
        method: method,
        body: params
    })
    
    if (error.value) {
        if(error.value.statusCode == 400)
        {
            const firstKey = Object.keys(error.value.data)[0]
            const firstValue = error.value.data[firstKey]
            if(firstValue[0] == "This field may not be blank.")
                alert("Preencha os campos obrigatórios.")
            if(firstValue[0] == "Enter a valid email address.")
                alert("Informe um e-mail válido.")
            if(firstValue[0] == "Enter a valid phone number.")
                alert("Informe um número de telefone válido.")
        }
    } else {
        alert("Usuário salvo com sucesso!")
        navigateTo('/usuarios')
    }   
    
}

</script>

<template>
    <div v-if="pending">Carregando...</div>
    <div v-else-if="error">Erro: {{ error.message }}</div>
    <GenericRegistration :item="item" :fields="listFields" title="Usuários" @voltar="Voltar" @salvar="Salvar" v-else/>
</template>
  