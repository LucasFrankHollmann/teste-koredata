<script setup>
    import {getParametersSearchList} from '@/js/GenericList.js'
    import { ref } from "vue"
    const emit = defineEmits(["search", "novoItem", "editarItem"]);
    const selectedRow = ref(null)

    defineProps({
        items: {
            type: Array,
            required: true
        },
        columns: {
            type: Object,
            required: true
        },
        title: {
            type: String,
            required: false
        }
    })

    async function SearchList(columns) {
        emit("search", await getParametersSearchList(columns));
    }
</script>

<style>

</style>

<template>
    <div class="centered-container">
        <div class= "list-content">
            <h1 v-if="title" class="list-title">{{title}}</h1><br v-if="title">
        
            <table>
                <colgroup>
                    <col v-for="col in columns" :style="{ width: col.width }"> 
                </colgroup>
                <thead>
                    <tr>
                        <th v-for="col in columns" class="list-header">
                            <div>
                                <p>{{ col.columnName }}</p>
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="list-search-bar">
                        <td v-for="col in columns">
                            <div class="list-search-bar-cell">
                                <input :id="'search-bar-input-' + col.propName" class="search-bar-input" :placeholder="'Buscar por ' + col.columnName" @keyup.enter="SearchList(columns)" ></input> 
                                <i class="list-search-icon fa-solid fa-magnifying-glass" @click="SearchList(columns)"></i>
                            </div>
                        </td>
                    </tr>

                    <tr v-for="(user, index) in items" @click="selectedRow = user.id" 
                        :key="user.id" 
                        :class="selectedRow === user.id ? 'list-row-highlight' : (index % 2 === 0 ? 'list-row-even' : 'list-row-odd')">

                        <td v-for="col in columns">
                            <div class="list-cell">
                                <p>{{ user[col.propName] }}</p>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        
            <div class="list-button-row">
                <button class="list-button" @click="$emit('editarItem', selectedRow)" v-if="selectedRow !== null">
                    editar
                    <i class="list-search-icon fa-solid fa-pen-to-square"></i>
                </button>
                <button class="list-button" @click="$emit('novoItem')">
                    novo
                    <i class="list-search-icon fa-solid fa-plus"></i>
                </button>
            </div>
        </div>
    </div>
</template>
  