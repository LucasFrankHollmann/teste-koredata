export async function getParametersSaveRegistration(fields)
{
    let params = {};
    fields.forEach(x => {
        params[x.propName] = document.getElementById('registration-input-' + x.propName)?.value
    });

    return params;
}

export async function preencherItem(item)
{
    for(let prop in item)
    {
        let input = document.getElementById('registration-input-' + prop)
        if(input !== null && input !== undefined)
            input.value = item[prop];
    }
}
