<template>
    <div v-if="error" class="alert alert-danger" role="alert">
        {{ error }}
    </div>
    <div v-else-if="success" class="alert alert-success" role="alert">
        {{ success }}
    </div>
</template>

<script>
export default {
    props: {
        error: {
            type: String,
            required: true,
        },
        success: {
            type: String,
            required: true,
        }
    }
}
</script>