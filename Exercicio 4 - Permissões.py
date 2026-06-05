permissões_funcionalidade = {'read', 'write', 'execute', 'admin'}
permissões_usuario = {'read', 'write', 'delete', 'delete'}
for permissão in permissões_funcionalidade:
    if permissão in permissões_usuario:
        print(f"O usuário tem a permissão: {permissão}")
    else:
        print(f"O usuário não tem a permissão: {permissão}")
#Por ser um conjunto, as permissões duplicadas serão automaticamente removidas, então 'delete' aparecerá apenas uma vez.
permissões_faltando = []

for permissão in permissões_funcionalidade:
    if permissão not in permissões_usuario:
        permissões_faltando.append(permissão)

print("Permissões faltando:", permissões_faltando)