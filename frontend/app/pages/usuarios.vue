<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'
const users = ref([]);
const config = useRuntimeConfig()
const router = useRouter()

let { data, pending, error } = await useFetch(
  `${config.public.apiBase}/users/filter`,
  { method: 'GET' }
)
users.value = data;
const listColumns = [
    {
        propName: "fullname",
        columnName: "Nome",
        width: "30%"
    },
    {
        propName: "email",
        columnName: "E-mail",
        width: "20%"
    },
    {
        propName: "adress",
        columnName: "Endereço",
        width: "35%"
    },
    {
        propName: "phone",
        columnName: "Telefone",
        width: "15%"
    },
]

async function NovoUsuario(){
    navigateTo('/cadastrousuario')
}

async function EditarUsuario(id){
    router.push({ name: 'cadastrousuario', query: { idUsuario: id } })
}

async function SearchUsers(params)
{
    let { data, pending, error } = await useFetch(
    `${config.public.apiBase}/users/filter`,
    { 
        method: 'GET',
        params: params

    })

    users.value = data;
    pending = pending;
    error = error;
}

</script>

<template>
    <div v-if="pending">Carregando...</div>
    <div v-else-if="error">Erro: {{ error.message }}</div>
    <GenericList :items="users.value" :columns="listColumns" title="Usuários"  @search="SearchUsers" @novoItem="NovoUsuario" @editarItem="EditarUsuario" v-else/>
</template>
  