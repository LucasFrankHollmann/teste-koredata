<script setup>
    import {getParametersSaveRegistration} from '@/js/GenericRegistration.js'
    import {preencherItem} from '@/js/GenericRegistration.js'
    const emit = defineEmits(["salvar", "voltar"]);

    const props = defineProps({
        fields: {
            type: Array,
            required: true
        },
        item: {
            type: Object,
            required: true
        },
        title: {
            type: String,
            required: false
        }
    })

    onMounted(() => {
        preencherItem(props.item)
    })

    async function SalvarItem(fields) {
        emit("salvar", await getParametersSaveRegistration(fields));
    }
</script>

<template>
    <div class="centered-container">
        <div class= "registration-content">
            <h1 v-if="title" class="list-title">{{title}}</h1><br v-if="title">
            <div class="centered-container">
                <div class="registration-form">
                    
                    <div class="registration-fields" v-for="field in fields">
                        <p>{{ field.fieldName }}</p>
                        <input :id="'registration-input-' + field.propName"></input>
                    </div>

                    <div class="registration-button-row">
                        <button class="registration-button" @click="$emit('voltar')">
                            voltar
                            <i class="list-search-icon fa-solid fa-arrow-left"></i>
                        </button>
                        <button class="registration-button" @click="SalvarItem(fields)">
                            salvar
                            <i class="list-search-icon fa-solid fa-save"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  